import FWCore.ParameterSet.Config as cms

def L1TStage1Layer2Producer(*args, **kwargs):
  mod = cms.EDProducer('L1TStage1Layer2Producer',
    CaloRegions = cms.required.InputTag,
    CaloEmCands = cms.required.InputTag,
    conditionsLabel = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
