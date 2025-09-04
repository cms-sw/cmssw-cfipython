import FWCore.ParameterSet.Config as cms

def DTCertificationSummary(*args, **kwargs):
  mod = cms.EDProducer('DTCertificationSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
