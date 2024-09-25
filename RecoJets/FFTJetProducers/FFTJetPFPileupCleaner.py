import FWCore.ParameterSet.Config as cms

def FFTJetPFPileupCleaner(*args, **kwargs):
  mod = cms.EDProducer('FFTJetPFPileupCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
