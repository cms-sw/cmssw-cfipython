import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorRecHit(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorRecHit',
    GlobalNRecHits = cms.PSet(
      name = cms.string('Num_RecHits'),
      title = cms.string(';Number of rechits per event;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(350000),
      NxBins = cms.int32(150)
    ),
    GlobalPositionXY_P = cms.PSet(
      name = cms.string('RecHit_Global_Position_XY_P'),
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
      name = cms.string('RecHit_Global_Position_XY_S'),
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
      name = cms.string('RecHit_Global_Position_RZ_P'),
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
      name = cms.string('RecHit_Global_Position_RZ_S'),
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
      name = cms.string('Num_RecHits_Layer_P'),
      title = cms.string('Number of RecHits per event in macro pixel sensors;'),
      xmin = cms.double(0),
      xmax = cms.double(28000),
      NxBins = cms.int32(150),
      switch = cms.bool(True)
    ),
    NRecHitsLayer_S = cms.PSet(
      name = cms.string('Num_RecHits_Layer_S'),
      title = cms.string('Number of RecHits per event in strip sensors;'),
      xmin = cms.double(0),
      xmax = cms.double(28000),
      NxBins = cms.int32(150),
      switch = cms.bool(True)
    ),
    RecHitSize_P = cms.PSet(
      name = cms.string('RecHit_Size_P'),
      title = cms.string('RecHit size in macro pixel sensors;RecHit size(macro pixel);'),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31),
      switch = cms.bool(True)
    ),
    RecHitSize_S = cms.PSet(
      name = cms.string('RecHit_Size_S'),
      title = cms.string('RecHit size in strip sensors;RecHit size(strips);'),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31),
      switch = cms.bool(True)
    ),
    TopFolderName = cms.string('OuterTracker'),
    Verbosity = cms.bool(False),
    rechitsSrc = cms.InputTag('siPhase2RecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
