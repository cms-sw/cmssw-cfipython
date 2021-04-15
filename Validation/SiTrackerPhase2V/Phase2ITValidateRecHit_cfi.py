import FWCore.ParameterSet.Config as cms

Phase2ITValidateRecHit = cms.EDProducer('Phase2ITValidateRecHit',
  DeltaX = cms.PSet(
    name = cms.string('Delta_X'),
    title = cms.string('Delta_X;RecHit resolution X coordinate [#mum]'),
    switch = cms.bool(True),
    xmin = cms.double(-100),
    xmax = cms.double(100),
    NxBins = cms.int32(100)
  ),
  DeltaY = cms.PSet(
    name = cms.string('Delta_Y'),
    title = cms.string('Delta_Y;RecHit resolution Y coordinate [#mum];'),
    switch = cms.bool(True),
    xmin = cms.double(-100),
    xmax = cms.double(100),
    NxBins = cms.int32(100)
  ),
  PullX = cms.PSet(
    name = cms.string('Pull_X'),
    title = cms.string('Pull_X;pull x;'),
    xmin = cms.double(-4),
    switch = cms.bool(True),
    xmax = cms.double(4),
    NxBins = cms.int32(100)
  ),
  PullY = cms.PSet(
    name = cms.string('Pull_Y'),
    title = cms.string('Pull_Y;pull y;'),
    xmin = cms.double(-4),
    switch = cms.bool(True),
    xmax = cms.double(4),
    NxBins = cms.int32(100)
  ),
  DeltaX_eta = cms.PSet(
    name = cms.string('Delta_X_vs_Eta'),
    title = cms.string('Delta_X_vs_Eta;#eta;#Delta x [#mum]'),
    ymin = cms.double(-100),
    ymax = cms.double(100),
    NxBins = cms.int32(82),
    switch = cms.bool(True),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1)
  ),
  DeltaY_eta = cms.PSet(
    name = cms.string('Delta_Y_vs_Eta'),
    title = cms.string('Delta_Y_vs_Eta;#eta;#Delta y [#mum]'),
    ymin = cms.double(-100),
    ymax = cms.double(100),
    NxBins = cms.int32(82),
    switch = cms.bool(True),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1)
  ),
  PullX_eta = cms.PSet(
    name = cms.string('Pull_X_vs_Eta'),
    title = cms.string('Pull_X_vs_Eta;#eta;pull x'),
    ymax = cms.double(4),
    NxBins = cms.int32(82),
    switch = cms.bool(True),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1),
    ymin = cms.double(-4)
  ),
  PullY_eta = cms.PSet(
    name = cms.string('Pull_Y_vs_Eta'),
    title = cms.string('Pull_Y_vs_Eta;#eta;pull y'),
    ymax = cms.double(4),
    NxBins = cms.int32(82),
    switch = cms.bool(True),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1),
    ymin = cms.double(-4)
  ),
  nRecHits_primary = cms.PSet(
    name = cms.string('Number_RecHits_matched_PrimarySimTrack'),
    title = cms.string('Number of RecHits matched to primary SimTrack;;'),
    xmin = cms.double(0),
    switch = cms.bool(True),
    xmax = cms.double(0),
    NxBins = cms.int32(100)
  ),
  DeltaX_primary = cms.PSet(
    name = cms.string('Delta_X_SimHitPrimary'),
    title = cms.string('Delta_X_SimHitPrimary;#delta x [#mum];'),
    xmin = cms.double(-100),
    switch = cms.bool(True),
    xmax = cms.double(100),
    NxBins = cms.int32(100)
  ),
  DeltaY_primary = cms.PSet(
    name = cms.string('Delta_Y_SimHitPrimary'),
    title = cms.string('Delta_Y_SimHitPrimary;#Delta y [#mum];'),
    xmin = cms.double(-100),
    switch = cms.bool(True),
    xmax = cms.double(100),
    NxBins = cms.int32(100)
  ),
  PullX_primary = cms.PSet(
    name = cms.string('Pull_X_SimHitPrimary'),
    title = cms.string('Pull_X_SimHitPrimary;pull x;'),
    ymax = cms.double(4),
    NxBins = cms.int32(82),
    switch = cms.bool(True),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1),
    ymin = cms.double(-4)
  ),
  PullY_primary = cms.PSet(
    name = cms.string('Pull_Y_SimHitPrimary'),
    title = cms.string('Pull_Y_SimHitPrimary;pull y;'),
    ymax = cms.double(4),
    NxBins = cms.int32(82),
    switch = cms.bool(True),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1),
    ymin = cms.double(-4)
  ),
  associatePixel = cms.bool(True),
  associateStrip = cms.bool(False),
  usePhase2Tracker = cms.bool(True),
  associateRecoTracks = cms.bool(False),
  associateHitbySimTrack = cms.bool(True),
  pixelSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Pixel'),
  ROUList = cms.vstring(
    'TrackerHitsPixelBarrelLowTof',
    'TrackerHitsPixelBarrelHighTof',
    'TrackerHitsPixelEndcapLowTof',
    'TrackerHitsPixelEndcapHighTof'
  ),
  simTracksSrc = cms.InputTag('g4SimHits'),
  SimVertexSource = cms.InputTag('g4SimHits'),
  SimTrackMinPt = cms.double(2),
  rechitsSrc = cms.InputTag('siPixelRecHits'),
  TopFolderName = cms.string('TrackerPhase2ITRecHitV'),
  Verbosity = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
