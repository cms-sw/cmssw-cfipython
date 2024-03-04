import FWCore.ParameterSet.Config as cms

def ProvenanceCheckerOutputModule(**kwargs):
  mod = cms.OutputModule('ProvenanceCheckerOutputModule',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
