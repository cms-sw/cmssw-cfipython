import FWCore.ParameterSet.Config as cms

def SimpleTrackValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('SimpleTrackValidation',
    trackLabels = cms.VInputTag('generalTracks'),
    trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
    trackAssociator = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    ptMinTP = cms.double(0.9),
    ptMaxTP = cms.double(1e+100),
    minRapidityTP = cms.double(-2.4),
    maxRapidityTP = cms.double(2.4),
    tipTP = cms.double(3.5),
    lipTP = cms.double(30),
    minHitTP = cms.int32(0),
    signalOnlyTP = cms.bool(True),
    intimeOnlyTP = cms.bool(False),
    chargedOnlyTP = cms.bool(True),
    stableOnlyTP = cms.bool(False),
    pdgIdTP = cms.vint32(),
    invertRapidityCutTP = cms.bool(False),
    minPhiTP = cms.double(-3.2),
    maxPhiTP = cms.double(3.2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
