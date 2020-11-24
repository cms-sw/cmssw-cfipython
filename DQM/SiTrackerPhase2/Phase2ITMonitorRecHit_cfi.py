import FWCore.ParameterSet.Config as cms

Phase2ITMonitorRecHit = cms.EDProducer('Phase2ITMonitorRecHit',
  GlobalNumberRecHits = cms.PSet(
    name = cms.string('NumberRecHits'),
    title = cms.string('NumberRecHits;Number of RecHits;'),
    xmin = cms.double(0),
    switch = cms.bool(True),
    xmax = cms.double(0),
    NxBins = cms.int32(50)
  ),
  GlobalPositionRZ_PXB = cms.PSet(
    name = cms.string('Global_Position_RZ_IT_barrel'),
    title = cms.string('Global_Position_RZ_IT_barrel;z [mm];r [mm]'),
    ymax = cms.double(300),
    NxBins = cms.int32(1500),
    NyBins = cms.int32(300),
    switch = cms.bool(True),
    xmax = cms.double(3000),
    xmin = cms.double(-3000),
    ymin = cms.double(0)
  ),
  GlobalPositionXY_PXB = cms.PSet(
    name = cms.string('Global_Position_XY_IT_barrel'),
    title = cms.string('Global_Position_XY_IT_barrel;x [mm];y [mm];'),
    ymax = cms.double(300),
    NxBins = cms.int32(600),
    NyBins = cms.int32(600),
    switch = cms.bool(True),
    xmax = cms.double(300),
    xmin = cms.double(-300),
    ymin = cms.double(-300)
  ),
  GlobalPositionRZ_PXEC = cms.PSet(
    name = cms.string('Global_Position_RZ_IT_endcap'),
    title = cms.string('Global_Position_RZ_IT_endcap;z [mm];r [mm]'),
    ymax = cms.double(300),
    NxBins = cms.int32(1500),
    NyBins = cms.int32(300),
    switch = cms.bool(True),
    xmax = cms.double(3000),
    xmin = cms.double(-3000),
    ymin = cms.double(0)
  ),
  GlobalPositionXY_PXEC = cms.PSet(
    name = cms.string('Global_Position_XY_IT_endcap'),
    title = cms.string('Global_Position_XY_IT_endcap; x [mm]; y [mm]'),
    ymax = cms.double(300),
    NxBins = cms.int32(600),
    NyBins = cms.int32(600),
    switch = cms.bool(True),
    xmax = cms.double(300),
    xmin = cms.double(-300),
    ymin = cms.double(-300)
  ),
  LocalNumberRecHits = cms.PSet(
    name = cms.string('LocalNumberRecHits'),
    title = cms.string('NumberRecHits;Number of RecHits;'),
    xmin = cms.double(0),
    switch = cms.bool(True),
    xmax = cms.double(0),
    NxBins = cms.int32(50)
  ),
  GlobalPositionRZ_perlayer = cms.PSet(
    name = cms.string('Global_Position_RZ'),
    title = cms.string('Global_Position_RZ;z [mm];r [mm]'),
    ymax = cms.double(300),
    NxBins = cms.int32(1500),
    NyBins = cms.int32(300),
    switch = cms.bool(False),
    xmax = cms.double(3000),
    xmin = cms.double(-3000),
    ymin = cms.double(0)
  ),
  GlobalPositionXY_perlayer = cms.PSet(
    name = cms.string('Global_Position_XY'),
    title = cms.string('Global_Position_XY;x [mm]; y[mm]'),
    ymax = cms.double(300),
    NxBins = cms.int32(600),
    NyBins = cms.int32(600),
    switch = cms.bool(False),
    xmax = cms.double(300),
    xmin = cms.double(-300),
    ymin = cms.double(-300)
  ),
  LocalPositionXY = cms.PSet(
    name = cms.string('Local_Position_XY'),
    title = cms.string('Local_Position_XY; x; y'),
    ymax = cms.double(0),
    NxBins = cms.int32(500),
    NyBins = cms.int32(500),
    switch = cms.bool(True),
    xmax = cms.double(0),
    xmin = cms.double(0),
    ymin = cms.double(0)
  ),
  LocalClusterSizeX = cms.PSet(
    name = cms.string('Cluster_SizeX'),
    title = cms.string('Cluster_SizeX; cluster size x;'),
    xmin = cms.double(-0.5),
    switch = cms.bool(True),
    xmax = cms.double(20.5),
    NxBins = cms.int32(21)
  ),
  LocalClusterSizeY = cms.PSet(
    name = cms.string('Cluster_SizeY'),
    title = cms.string('Cluster_SizeY;cluster size y;'),
    xmin = cms.double(-0.5),
    switch = cms.bool(True),
    xmax = cms.double(20.5),
    NxBins = cms.int32(21)
  ),
  RecHitPosX = cms.PSet(
    name = cms.string('RecHit_X'),
    title = cms.string('RecHit_X;RecHit position X dimension;'),
    xmin = cms.double(-2.5),
    switch = cms.bool(True),
    xmax = cms.double(2.5),
    NxBins = cms.int32(100)
  ),
  RecHitPosY = cms.PSet(
    name = cms.string('RecHit_Y'),
    title = cms.string('RecHit_Y;RecHit position X dimension;'),
    xmin = cms.double(-2.5),
    switch = cms.bool(True),
    xmax = cms.double(2.5),
    NxBins = cms.int32(100)
  ),
  RecHitPosErrorX_Eta = cms.PSet(
    name = cms.string('RecHit_X_error_Vs_eta'),
    title = cms.string('RecHit_X_error_Vs_eta;#eta;x error #times 10^{6}'),
    switch = cms.bool(True),
    NxBins = cms.int32(82),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1),
    ymax = cms.double(10),
    ymin = cms.double(0)
  ),
  RecHitPosErrorY_Eta = cms.PSet(
    name = cms.string('RecHit_Y_error_Vs_eta'),
    title = cms.string('RecHit_Y_error_Vs_eta;#eta;y error #times 10^{6}'),
    switch = cms.bool(True),
    NxBins = cms.int32(82),
    xmax = cms.double(4.1),
    xmin = cms.double(-4.1),
    ymax = cms.double(10),
    ymin = cms.double(0)
  ),
  TopFolderName = cms.string('TrackerPhase2ITRecHit'),
  rechitsSrc = cms.InputTag('siPixelRecHits'),
  mightGet = cms.optional.untracked.vstring
)
