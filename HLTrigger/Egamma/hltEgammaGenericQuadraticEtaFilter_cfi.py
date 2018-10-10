import FWCore.ParameterSet.Config as cms

hltEgammaGenericQuadraticEtaFilter = cms.EDFilter('HLTEgammaGenericQuadraticEtaFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltEGIsolFilter'),
  varTag = cms.InputTag('hltEGIsol'),
  rhoTag = cms.InputTag(''),
  energyLowEdges = cms.vdouble(0),
  lessThan = cms.bool(True),
  useEt = cms.bool(True),
  etaBoundaryEB12 = cms.double(1),
  etaBoundaryEE12 = cms.double(2),
  thrRegularEB1 = cms.vdouble(4),
  thrRegularEE1 = cms.vdouble(6),
  thrOverEEB1 = cms.vdouble(0.002),
  thrOverEEE1 = cms.vdouble(0.002),
  thrOverE2EB1 = cms.vdouble(0),
  thrOverE2EE1 = cms.vdouble(0),
  thrRegularEB2 = cms.vdouble(6),
  thrRegularEE2 = cms.vdouble(4),
  thrOverEEB2 = cms.vdouble(0.002),
  thrOverEEE2 = cms.vdouble(0.002),
  thrOverE2EB2 = cms.vdouble(0),
  thrOverE2EE2 = cms.vdouble(0),
  ncandcut = cms.int32(1),
  doRhoCorrection = cms.bool(False),
  rhoMax = cms.double(99999999),
  rhoScale = cms.double(1),
  effectiveAreas = cms.vdouble(
    0,
    0
  ),
  absEtaLowEdges = cms.vdouble(
    0,
    1.479
  ),
  l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate')
)
