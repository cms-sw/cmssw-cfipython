import FWCore.ParameterSet.Config as cms

def FFTJetPileupEstimator(**kwargs):
  mod = cms.EDProducer('FFTJetPileupEstimator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
