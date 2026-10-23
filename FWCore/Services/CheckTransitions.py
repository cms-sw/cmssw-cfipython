import FWCore.ParameterSet.Config as cms

def CheckTransitions(*args, **kwargs):
  mod = cms.Service('CheckTransitions',
    transitions = cms.untracked.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        type = cms.required.untracked.string,
        id = cms.required.untracked.EventID
      )
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
