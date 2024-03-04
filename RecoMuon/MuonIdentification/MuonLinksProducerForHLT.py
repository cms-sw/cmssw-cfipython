import FWCore.ParameterSet.Config as cms

def MuonLinksProducerForHLT(**kwargs):
  mod = cms.EDProducer('MuonLinksProducerForHLT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
