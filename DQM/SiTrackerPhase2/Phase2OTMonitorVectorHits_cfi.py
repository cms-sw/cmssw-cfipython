import FWCore.ParameterSet.Config as cms

Phase2OTMonitorVectorHits = cms.EDProducer('Phase2OTMonitorVectorHits',
  GlobalNVecHits = cms.PSet(
    name = cms.string('NumberOfVecHits'),
    title = cms.string(';Number of vechits per event;'),
    xmin = cms.double(0),
    switch = cms.bool(True),
    xmax = cms.double(15000),
    NxBins = cms.int32(150)
  ),
  GlobalPositionXY_P = cms.PSet(
    name = cms.string('Global_VecHitPosition_XY_P'),
    title = cms.string('Global_VecHitPosition_XY_P;x [mm];y [mm];'),
    NxBins = cms.int32(1250),
    xmin = cms.double(-1250),
    xmax = cms.double(1250),
    NyBins = cms.int32(1250),
    ymin = cms.double(-1250),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  GlobalPositionXY_S = cms.PSet(
    name = cms.string('Global_VecHitPosition_XY_S'),
    title = cms.string('Global_VecHitPosition_XY_S;x [mm];y [mm];'),
    NxBins = cms.int32(1250),
    xmin = cms.double(-1250),
    xmax = cms.double(1250),
    NyBins = cms.int32(1250),
    ymin = cms.double(-1250),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  GlobalPositionRZ_P = cms.PSet(
    name = cms.string('Global_VecHitPosition_RZ_P'),
    title = cms.string('Global_VecHitPosition_RZ_P;z [mm];r [mm]'),
    NxBins = cms.int32(1500),
    xmin = cms.double(-3000),
    xmax = cms.double(3000),
    NyBins = cms.int32(1250),
    ymin = cms.double(0),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  GlobalPositionRZ_S = cms.PSet(
    name = cms.string('Global_VecHitPosition_RZ_S'),
    title = cms.string('Global_VecHitPosition_RZ_S;z [mm];r [mm]'),
    NxBins = cms.int32(1500),
    xmin = cms.double(-3000),
    xmax = cms.double(3000),
    NyBins = cms.int32(1250),
    ymin = cms.double(0),
    ymax = cms.double(1250),
    switch = cms.bool(True)
  ),
  NVecHitsLayer_P = cms.PSet(
    name = cms.string('NumberOfVecHitsLayerP'),
    title = cms.string(';Number of vector hits per event(macro pixel sensor);'),
    xmin = cms.double(0),
    xmax = cms.double(5000),
    NxBins = cms.int32(100),
    switch = cms.bool(True)
  ),
  NVecHitsLayer_S = cms.PSet(
    name = cms.string('NumberOfVecHitsLayerS'),
    title = cms.string(';Number of vector hits per event(strip sensor);'),
    xmin = cms.double(0),
    xmax = cms.double(5000),
    NxBins = cms.int32(100),
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
  Curvature = cms.PSet(
    name = cms.string('CurvatureOfVecHits'),
    title = cms.string(';VectorHit curvature;'),
    xmin = cms.double(-0.05),
    switch = cms.bool(True),
    xmax = cms.double(0.05),
    NxBins = cms.int32(200)
  ),
  CurvErr = cms.PSet(
    name = cms.string('CurvatureErrOCurvature'),
    title = cms.string(';VectorHit #delta#rho/#rho;'),
    xmin = cms.double(-0.05),
    switch = cms.bool(True),
    xmax = cms.double(0.05),
    NxBins = cms.int32(500)
  ),
  Phi = cms.PSet(
    name = cms.string('PhiOfVecHits'),
    title = cms.string(';VectorHit #phi;'),
    xmin = cms.double(-3.1415926535897931),
    switch = cms.bool(True),
    xmax = cms.double(3.1415926535897931),
    NxBins = cms.int32(30)
  ),
  Eta = cms.PSet(
    name = cms.string('EtaOfVecHits'),
    title = cms.string(';VectorHit #eta;'),
    xmin = cms.double(-5),
    switch = cms.bool(True),
    xmax = cms.double(5),
    NxBins = cms.int32(50)
  ),
  Pt = cms.PSet(
    name = cms.string('PtOfVecHits'),
    title = cms.string('VectorHit p_T;p_T ;'),
    NxBins = cms.int32(100),
    xmin = cms.double(0),
    xmax = cms.double(200),
    switch = cms.bool(True)
  ),
  Chi2 = cms.PSet(
    name = cms.string('Chi2OfVecHits'),
    title = cms.string('VectorHit chi squared; #chi^2;'),
    NxBins = cms.int32(100),
    xmin = cms.double(0),
    xmax = cms.double(1e-06),
    switch = cms.bool(True)
  ),
  CurvatureVsEta_P = cms.PSet(
    name = cms.string('CurvatureVsEtaProf_P'),
    title = cms.string('Curvature vs #eta (macro-pixel);#eta ;curvature ;'),
    NxBins = cms.int32(50),
    xmin = cms.double(-5),
    xmax = cms.double(5),
    ymin = cms.double(-0.05),
    ymax = cms.double(0.05),
    switch = cms.bool(True)
  ),
  CurvatureVsEta_S = cms.PSet(
    name = cms.string('CurvatureVsEtaProf_S'),
    title = cms.string('Curvature vs #eta (strip);#eta ;curvature ;'),
    NxBins = cms.int32(25),
    xmin = cms.double(-5),
    xmax = cms.double(5),
    ymin = cms.double(-0.05),
    ymax = cms.double(0.05),
    switch = cms.bool(True)
  ),
  TopFolderName = cms.string('TrackerPhase2OTVectorHits/Accepted'),
  Verbosity = cms.bool(False),
  vechitsSrc = cms.InputTag('siPhase2VectorHits', 'accepted'),
  mightGet = cms.optional.untracked.vstring
)
