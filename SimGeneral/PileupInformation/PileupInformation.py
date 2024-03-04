import FWCore.ParameterSet.Config as cms

def PileupInformation(**kwargs):
  mod = cms.EDProducer('PileupInformation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
