import FWCore.ParameterSet.Config as cms

def HLTMuonCertSummary(**kwargs):
  mod = cms.EDProducer('HLTMuonCertSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
