import FWCore.ParameterSet.Config as cms

def DTCertificationSummary(**kwargs):
  mod = cms.EDProducer('DTCertificationSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
