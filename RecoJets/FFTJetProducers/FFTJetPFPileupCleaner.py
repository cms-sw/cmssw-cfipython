import FWCore.ParameterSet.Config as cms

def FFTJetPFPileupCleaner(**kwargs):
  mod = cms.EDProducer('FFTJetPFPileupCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
