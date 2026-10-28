import FWCore.ParameterSet.Config as cms

def Phase2ITMonitorRecHit(*args, **kwargs):
  mod = cms.EDProducer('Phase2ITMonitorRecHit',
    GlobalPositionRZ_PXB = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_RZ_IT_barrel'),
      title = cms.string('RecHit_Global_Position_RZ_IT_barrel;z [mm];r [mm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-3000),
      xmax = cms.double(3000),
      NyBins = cms.int32(300),
      ymin = cms.double(0),
      ymax = cms.double(300)
    ),
    GlobalPositionXY_PXB = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_XY_IT_barrel'),
      title = cms.string('RecHit_Global_Position_XY_IT_barrel;x [mm];y [mm]'),
      NxBins = cms.int32(600),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(600),
      ymin = cms.double(-300),
      ymax = cms.double(300)
    ),
    GlobalPositionRZ_PXEC = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_RZ_IT_endcap'),
      title = cms.string('RecHit_Global_Position_RZ_IT_endcap;z [mm];r [mm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-3000),
      xmax = cms.double(3000),
      NyBins = cms.int32(300),
      ymin = cms.double(0),
      ymax = cms.double(300)
    ),
    GlobalPositionXY_PXEC = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Global_Position_XY_IT_endcap'),
      title = cms.string('RecHit_Global_Position_XY_IT_endcap;x [mm];y [mm]'),
      NxBins = cms.int32(600),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(600),
      ymin = cms.double(-300),
      ymax = cms.double(300)
    ),
    LocalNumberRecHits = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_RecHits_Per_Event'),
      title = cms.string('Number of RecHits per event in {};Number of RecHits;Number of events'),
      NxBins = cms.int32(150),
      xmin = cms.double(0),
      xmax = cms.double(250000)
    ),
    LocalClusterSizeX = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Size_X'),
      title = cms.string('RecHit size in X dimension in {};RecHit size x;Number of RecHits'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    LocalClusterSizeY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Size_Y'),
      title = cms.string('RecHit size in Y dimension in {};RecHit size y;Number of RecHits'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    RecHitPosX = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_X'),
      title = cms.string('RecHit position in X dimension in {};RecHit position X dimension;Number of RecHits'),
      NxBins = cms.int32(100),
      xmin = cms.double(-2.5),
      xmax = cms.double(2.5)
    ),
    RecHitPosY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Y'),
      title = cms.string('RecHit position in Y dimension in {};RecHit position Y dimension;Number of RecHits'),
      NxBins = cms.int32(100),
      xmin = cms.double(-2.5),
      xmax = cms.double(2.5)
    ),
    RecHitPosErrorX_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_X_error_Vs_eta'),
      title = cms.string('RecHit X error Vs eta in {};#eta;x error [#mum]'),
      NxBins = cms.int32(82),
      xmin = cms.double(-4.1),
      xmax = cms.double(4.1),
      NyBins = cms.int32(0),
      ymin = cms.double(0),
      ymax = cms.double(10)
    ),
    RecHitPosErrorY_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('RecHit_Y_error_Vs_eta'),
      title = cms.string('RecHit Y error Vs eta in {};#eta;y error [#mum]'),
      NxBins = cms.int32(82),
      xmin = cms.double(-4.1),
      xmax = cms.double(4.1),
      NyBins = cms.int32(0),
      ymin = cms.double(0),
      ymax = cms.double(10)
    ),
    TopFolderName = cms.string('InnerTracker'),
    rechitsSrc = cms.InputTag('siPixelRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
