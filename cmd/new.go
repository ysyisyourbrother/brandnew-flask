package cmd

import (
	"embed"
	"fmt"
	"io/fs"
	"os"
	"path"
	"text/template"

	survey "github.com/AlecAivazis/survey/v2"
	"github.com/spf13/cobra"
)

var (
	newCmd = &cobra.Command{
		Use:   "new",
		Short: "Create flask-app",
		Long: `Create a brandnew-flask based flask application,
		which follows the MVC specification and 
		support the production environment`,
		RunE: newFlask,
	}
	//go:embed templates/* templates/*/* templates/*/*/*
	tmplFS  embed.FS
	tmplDir string = "templates"
)

type projectInfo struct {
	Name   string // flask-app name
	Author string // author name
}

// Interaction
func runSurvey() (*projectInfo, error) {
	var err error
	args := &projectInfo{}
	qsProName := []*survey.Question{
		{
			Name: "name",
			Prompt: &survey.Input{
				Message: "Your flask-app name:",
				Default: "myapp",
			},
			Validate: survey.Required,
		},
		{
			Name: "author",
			Prompt: &survey.Input{
				Message: "Your name:",
				Default: "anonym",
			},
			Validate: survey.Required,
		},
	}
	err = survey.Ask(qsProName, args)
	if err != nil {
		return nil, err
	}
	return args, nil
}

// Create project file/dir and render template
func createAndRender(dirEntries []fs.DirEntry, p *projectInfo, prefix string) (err error) {
	for _, de := range dirEntries {
		tmpl_path := path.Join(tmplDir, prefix, de.Name())
		output_path := path.Join(p.Name, prefix, de.Name())
		if de.IsDir() { // dir
			_dirEntries, err := tmplFS.ReadDir(tmpl_path)
			if err != nil {
				return err
			}
			os.Mkdir(output_path, os.ModePerm)
			_ = createAndRender(_dirEntries, p, path.Join(prefix, de.Name()))
		} else { // tmpl file
			tmpl, err := template.ParseFS(tmplFS, tmpl_path)
			if err != nil {
				return err
			}
			file, err := os.Create(output_path)
			if err != nil {
				return err
			}
			err = tmpl.Execute(file, p)
			if err != nil {
				return err
			}
		}
	}
	return
}

func newFlask(cmd *cobra.Command, args []string) error {
	p, err := runSurvey()
	if err != nil {
		return err
	}

	os.Mkdir(p.Name, os.ModePerm)
	dirEntries, err := tmplFS.ReadDir(tmplDir)
	if err != nil {
		return err
	}

	err = createAndRender(dirEntries, p, "")
	if err != nil {
		return err
	}
	fmt.Printf("Flask-app %s created successfully!\n", p.Name)

	return nil
}
