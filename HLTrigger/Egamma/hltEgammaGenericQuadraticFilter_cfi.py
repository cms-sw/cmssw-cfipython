import FWCore.ParameterSet.Config as cms

hltEgammaGenericQuadraticFilter = cms.EDFilter('HLTEgammaGenericQuadraticFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltSingleEgammaEtFilter'),
  isoTag = cms.InputTag('hltSingleEgammaHcalIsol'),
  nonIsoTag = cms.InputTag('hltSingleEgammaHcalNonIsol'),
  lessThan = cms.bool(True),
  useEt = cms.bool(False),
  thrRegularEB = cms.double(0),
  thrRegularEE = cms.double(0),
  thrOverEEB = cms.double(0),
  thrOverEEE = cms.double(0),
  thrOverE2EB = cms.double(0),
  thrOverE2EE = cms.double(0),
  ncandcut = cms.int32(1),
  doIsolated = cms.bool(True),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate')
)
