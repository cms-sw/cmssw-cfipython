import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingJet(*args, **kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingJet',
    dataTag = cms.required.InputTag,
    selectBxs = cms.required.InputTag,
    productLabel = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
