import FWCore.ParameterSet.Config as cms

def SiStripRecHitConverter(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
