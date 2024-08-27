import FWCore.ParameterSet.Config as cms

def CaloMuonMerger(**kwargs):
  mod = cms.EDProducer('CaloMuonMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
