import FWCore.ParameterSet.Config as cms

def ProvenanceCheckerOutputModule(*args, **kwargs):
  mod = cms.OutputModule('ProvenanceCheckerOutputModule',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
