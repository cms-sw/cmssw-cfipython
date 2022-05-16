import FWCore.ParameterSet.Config as cms

Phase2OTMonitorRecHit = cms.EDProducer('Phase2OTMonitorRecHit',
  GlobalNRecHits = cms.PSet(
    name = cms.string('NumberOfRecHits'),
    title = cms.string(';Number of rechits per event;'),
    xmin = cms.double(0),
    switch = cms.bool(True),
    xmax = cms.double(0),
    NxBins = cms.int32(150)
  ),
  GlobalPositionXY_P = cms.PSet(
    name = cms.string('Global_RecHitPosition_XY_P'),
    title = cms.string('Global_RecHitPosition_XY_P;x [mm];y [mm];'),
    NxBins = cms.int32(1250),
    xmin = cms.double(-1250),
    xmax = cms.double(1250),
    NyBins = cms.int32(1250),
    ymin = cms.double(-1250),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  GlobalPositionXY_S = cms.PSet(
    name = cms.string('Global_RecHitPosition_XY_S'),
    title = cms.string('Global_RecHitPosition_XY_S;x [mm];y [mm];'),
    NxBins = cms.int32(1250),
    xmin = cms.double(-1250),
    xmax = cms.double(1250),
    NyBins = cms.int32(1250),
    ymin = cms.double(-1250),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  GlobalPositionRZ_P = cms.PSet(
    name = cms.string('Global_RecHitPosition_RZ_P'),
    title = cms.string('Global_RecHitPosition_RZ_P;z [mm];r [mm]'),
    NxBins = cms.int32(1500),
    xmin = cms.double(-3000),
    xmax = cms.double(3000),
    NyBins = cms.int32(1250),
    ymin = cms.double(0),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  GlobalPositionRZ_S = cms.PSet(
    name = cms.string('Global_RecHitPosition_RZ_S'),
    title = cms.string('Global_RecHitPosition_RZ_S;z [mm];r [mm]'),
    NxBins = cms.int32(1500),
    xmin = cms.double(-3000),
    xmax = cms.double(3000),
    NyBins = cms.int32(1250),
    ymin = cms.double(0),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  NRecHitsLayer_P = cms.PSet(
    name = cms.string('NumberOfRecHitsLayerP'),
    title = cms.string(';Number of clusters per event(macro pixel sensor);'),
    xmin = cms.double(0),
    xmax = cms.double(28000),
    NxBins = cms.int32(150),
    switch = cms.bool(True)
  ),
  NRecHitsLayer_S = cms.PSet(
    name = cms.string('NumberOfRecHitsLayerS'),
    title = cms.string(';Number of clusters per event(strip sensor);'),
    xmin = cms.double(0),
    xmax = cms.double(28000),
    NxBins = cms.int32(150),
    switch = cms.bool(True)
  ),
  ClusterSize_P = cms.PSet(
    name = cms.string('ClusterSize_P'),
    title = cms.string(';cluster size(macro pixel sensor);'),
    xmin = cms.double(-0.5),
    xmax = cms.double(30.5),
    NxBins = cms.int32(31),
    switch = cms.bool(True)
  ),
  ClusterSize_S = cms.PSet(
    name = cms.string('ClusterSize_S'),
    title = cms.string(';cluster size(strip sensor);'),
    xmin = cms.double(-0.5),
    xmax = cms.double(30.5),
    NxBins = cms.int32(31),
    switch = cms.bool(True)
  ),
  GlobalPositionXY_perlayer_P = cms.PSet(
    name = cms.string('GlobalPositionXY_perlayer_P'),
    title = cms.string('GlobalRecHitPositionXY_perlayer_P;x[mm];y[mm];'),
    NxBins = cms.int32(1250),
    xmin = cms.double(-1250),
    xmax = cms.double(1250),
    NyBins = cms.int32(1250),
    ymin = cms.double(-1250),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  GlobalPositionXY_perlayer_S = cms.PSet(
    name = cms.string('GlobalPositionXY_perlayer_S'),
    title = cms.string('GlobalRecHitPositionXY_perlayer_S;x[mm];y[mm];'),
    NxBins = cms.int32(1250),
    xmin = cms.double(-1250),
    xmax = cms.double(1250),
    NyBins = cms.int32(1250),
    ymin = cms.double(-1250),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  LocalPositionXY_P = cms.PSet(
    name = cms.string('LocalPositionXY_P'),
    title = cms.string('LocalPositionXY_P;x ;y ;'),
    NxBins = cms.int32(50),
    xmin = cms.double(-10),
    xmax = cms.double(10),
    NyBins = cms.int32(50),
    ymin = cms.double(-10),
    ymax = cms.double(10),
    switch = cms.bool(True)
  ),
  LocalPositionXY_S = cms.PSet(
    name = cms.string('LocalPositionXY_S'),
    title = cms.string('LocalPositionXY_S;x ;y ;'),
    NxBins = cms.int32(50),
    xmin = cms.double(-10),
    xmax = cms.double(10),
    NyBins = cms.int32(50),
    ymin = cms.double(-10),
    ymax = cms.double(10),
    switch = cms.bool(True)
  ),
  TopFolderName = cms.string('TrackerPhase2OTRecHit'),
  Verbosity = cms.bool(False),
  rechitsSrc = cms.InputTag('siPhase2RecHits'),
  mightGet = cms.optional.untracked.vstring
)
