import FWCore.ParameterSet.Config as cms

def SiStripRecHitConverter(*args, **kwargs):
  mod = cms.EDProducer('SiStripRecHitConverter',
    ClusterProducer = cms.InputTag('siStripClusters'),
    rphiRecHits = cms.string('rphiRecHit'),
    stereoRecHits = cms.string('stereoRecHit'),
    matchedRecHits = cms.string('matchedRecHit'),
    useSiStripQuality = cms.bool(False),
    MaskBadAPVFibers = cms.bool(False),
    doMatching = cms.bool(True),
    StripCPE = cms.ESInputTag('StripCPEfromTrackAngleESProducer', 'StripCPEfromTrackAngle'),
    Matcher = cms.ESInputTag('SiStripRecHitMatcherESProducer', 'StandardMatcher'),
    siStripQualityLabel = cms.ESInputTag('', ''),
    VerbosityLevel = cms.optional.untracked.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
