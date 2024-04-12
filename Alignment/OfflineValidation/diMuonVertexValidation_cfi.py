import FWCore.ParameterSet.Config as cms

diMuonVertexValidation = cms.EDAnalyzer('DiMuonVertexValidation',
  useReco = cms.bool(True),
  muons = cms.InputTag('muons'),
  decayMotherName = cms.string('Z'),
  tracks = cms.InputTag('generalTracks'),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  pTThresholds = cms.vdouble(
    30,
    10
  ),
  useClosestVertex = cms.bool(True),
  maxSVdist = cms.double(50),
  DiMuMassConfig = cms.PSet(
    name = cms.string('DiMuMass'),
    title = cms.string('M(#mu#mu)'),
    yUnits = cms.string('[GeV]'),
    NxBins = cms.int32(24),
    NyBins = cms.int32(50),
    ymin = cms.double(70),
    ymax = cms.double(120)
  ),
  CosPhiConfig = cms.PSet(
    name = cms.string('CosPhi'),
    title = cms.string('cos(#phi_{xy})'),
    yUnits = cms.string(''),
    NxBins = cms.int32(50),
    NyBins = cms.int32(50),
    ymin = cms.double(-1),
    ymax = cms.double(1)
  ),
  CosPhi3DConfig = cms.PSet(
    name = cms.string('CosPhi3D'),
    title = cms.string('cos(#phi_{3D})'),
    yUnits = cms.string(''),
    NxBins = cms.int32(50),
    NyBins = cms.int32(50),
    ymin = cms.double(-1),
    ymax = cms.double(1)
  ),
  VtxProbConfig = cms.PSet(
    name = cms.string('VtxProb'),
    title = cms.string('Prob(#chi^{2}_{SV})'),
    yUnits = cms.string(''),
    NxBins = cms.int32(50),
    NyBins = cms.int32(50),
    ymin = cms.double(0),
    ymax = cms.double(1)
  ),
  VtxDistConfig = cms.PSet(
    name = cms.string('VtxDist'),
    title = cms.string('d_{xy}(PV,SV)'),
    yUnits = cms.string('[#mum]'),
    NxBins = cms.int32(50),
    NyBins = cms.int32(100),
    ymin = cms.double(0),
    ymax = cms.double(300)
  ),
  VtxDist3DConfig = cms.PSet(
    name = cms.string('VtxDist3D'),
    title = cms.string('d_{3D}(PV,SV)'),
    yUnits = cms.string('[#mum]'),
    NxBins = cms.int32(50),
    NyBins = cms.int32(250),
    ymin = cms.double(0),
    ymax = cms.double(500)
  ),
  VtxDistSigConfig = cms.PSet(
    name = cms.string('VtxDistSig'),
    title = cms.string('d_{xy}(PV,SV)/#sigma_{dxy}(PV,SV)'),
    yUnits = cms.string(''),
    NxBins = cms.int32(50),
    NyBins = cms.int32(100),
    ymin = cms.double(0),
    ymax = cms.double(5)
  ),
  VtxDist3DSigConfig = cms.PSet(
    name = cms.string('VtxDist3DSig'),
    title = cms.string('d_{3D}(PV,SV)/#sigma_{d3D}(PV,SV)'),
    yUnits = cms.string(''),
    NxBins = cms.int32(50),
    NyBins = cms.int32(100),
    ymin = cms.double(0),
    ymax = cms.double(5)
  ),
  mightGet = cms.optional.untracked.vstring
)
