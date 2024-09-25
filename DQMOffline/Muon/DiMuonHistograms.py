import FWCore.ParameterSet.Config as cms

def DiMuonHistograms(*args, **kwargs):
  mod = cms.EDProducer('DiMuonHistograms',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
