import FWCore.ParameterSet.Config as cms

def CheckTransitions(**kwargs):
  mod = cms.Service('CheckTransitions',
    transitions = cms.untracked.VPSet(
      cms.PSet()
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
