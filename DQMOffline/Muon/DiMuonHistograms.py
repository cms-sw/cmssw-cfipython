import FWCore.ParameterSet.Config as cms

def DiMuonHistograms(**kwargs):
  mod = cms.EDProducer('DiMuonHistograms',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
