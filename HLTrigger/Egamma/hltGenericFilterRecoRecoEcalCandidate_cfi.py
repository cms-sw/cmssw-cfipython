import FWCore.ParameterSet.Config as cms

hltGenericFilterRecoRecoEcalCandidate = cms.EDFilter('HLTEgammaGenericFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltSingleEgammaEtFilter'),
  varTag = cms.InputTag('hltSingleEgammaHcalIsol'),
  rhoTag = cms.InputTag(''),
  energyLowEdges = cms.vdouble(0),
  lessThan = cms.bool(True),
  useEt = cms.bool(False),
  thrRegularEB = cms.vdouble(0),
  thrRegularEE = cms.vdouble(0),
  thrOverEEB = cms.vdouble(-1),
  thrOverEEE = cms.vdouble(-1),
  thrOverE2EB = cms.vdouble(-1),
  thrOverE2EE = cms.vdouble(-1),
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
