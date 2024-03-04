import FWCore.ParameterSet.Config as cms

def FFTJetPileupProcessor(**kwargs):
  mod = cms.EDProducer('FFTJetPileupProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
