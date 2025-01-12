import FWCore.ParameterSet.Config as cms

def Phase2TrackerRecHits(*args, **kwargs):
  mod = cms.EDProducer('Phase2TrackerRecHits',
    Phase2StripCPE = cms.ESInputTag('phase2StripCPEESProducer', 'Phase2StripCPE'),
    src = cms.InputTag('siPhase2Clusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
