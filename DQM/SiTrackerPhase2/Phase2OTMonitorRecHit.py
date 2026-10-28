import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorRecHit(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorRecHit',
    GlobalPositionXY_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_XY_P'),
      title = cms.string('Global_RecHitPosition_XY_P;x [mm];y [mm]'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-1250),
      xmax = cms.double(1250),
      NyBins = cms.int32(1250),
      ymin = cms.double(-1250),
      ymax = cms.double(1250)
    ),
    GlobalPositionXY_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_XY_S'),
      title = cms.string('Global_RecHitPosition_XY_S;x [mm];y [mm]'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-1250),
      xmax = cms.double(1250),
      NyBins = cms.int32(1250),
      ymin = cms.double(-1250),
      ymax = cms.double(1250)
    ),
    GlobalPositionRZ_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_RZ_P'),
      title = cms.string('Global_RecHitPosition_RZ_P;z [mm];r [mm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-3000),
      xmax = cms.double(3000),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(1250)
    ),
    GlobalPositionRZ_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_RZ_S'),
      title = cms.string('Global_RecHitPosition_RZ_S;z [mm];r [mm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-3000),
      xmax = cms.double(3000),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(1250)
    ),
    NRecHitsLayer_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_RecHits_Per_Event_P'),
      title = cms.string('Number of RecHits per event in pixels in {};Number of rechits;Number of events'),
      NxBins = cms.int32(150),
      xmin = cms.double(0),
      xmax = cms.double(300000)
    ),
    NRecHitsLayer_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_RecHits_Per_Event_S'),
      title = cms.string('Number of RecHits per event in strips in {};Number of rechits;Number of events'),
      NxBins = cms.int32(150),
      xmin = cms.double(0),
      xmax = cms.double(300000)
    ),
    RecHitSize_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Size_P'),
      title = cms.string('RecHit size in pixels in {};RecHit size (macro pixel);'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    RecHitSize_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Size_S'),
      title = cms.string('RecHit size in strips in {};RecHit size (strips);'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
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
