import FWCore.ParameterSet.Config as cms

def CosmicGridTripletSeeder(*args, **kwargs):
  mod = cms.EDProducer('CosmicGridTripletSeeder',
    vectorHits = cms.untracked.InputTag('siPhase2VectorHits', 'accepted'),
    OTRecHits = cms.untracked.InputTag('siPhase2RecHits'),
    matchedStripHits = cms.untracked.InputTag('siStripMatchedRecHits', 'matchedRecHit'),
    rPhiHits = cms.untracked.InputTag('siStripMatchedRecHits', 'rphiRecHit'),
    PixelRecHits = cms.untracked.InputTag('siPixelRecHits'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    MagneticFieldRecord = cms.ESInputTag('', ''),
    writeTriplets = cms.bool(False),
    nGridBinsX = cms.int32(1),
    nGridBinsY = cms.int32(1),
    nGridBinsZ = cms.int32(1),
    gridXmin = cms.double(-120),
    gridXmax = cms.double(120),
    gridYmin = cms.double(-120),
    gridYmax = cms.double(120),
    gridZmin = cms.double(-280),
    gridZmax = cms.double(280),
    maxTripsPerSP = cms.int32(10),
    maxSeedsPerSP = cms.int32(8),
    slopeCompatForVH = cms.double(0.15),
    tryBothDirections = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
