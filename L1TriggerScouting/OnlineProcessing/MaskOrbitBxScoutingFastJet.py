import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingFastJet(*args, **kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingFastJet',
    dataTag = cms.required.InputTag,
    selectBxs = cms.required.InputTag,
    productLabel = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
