import FWCore.ParameterSet.Config as cms

def VectorHitsBuilderValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('VectorHitsBuilderValidation',
    src = cms.string('siPhase2Clusters'),
    links = cms.InputTag('simSiPixelDigis', 'Tracker'),
    VH_acc = cms.InputTag('siPhase2VectorHits', 'accepted'),
    VH_rej = cms.InputTag('siPhase2VectorHits', 'rejected'),
    CPE = cms.ESInputTag('phase2StripCPEESProducer', 'Phase2StripCPE'),
    trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
