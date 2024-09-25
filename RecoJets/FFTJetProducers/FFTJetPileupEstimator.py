import FWCore.ParameterSet.Config as cms

def FFTJetPileupEstimator(*args, **kwargs):
  mod = cms.EDProducer('FFTJetPileupEstimator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
