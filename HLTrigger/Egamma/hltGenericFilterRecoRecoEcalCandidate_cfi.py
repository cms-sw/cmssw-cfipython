import FWCore.ParameterSet.Config as cms

hltGenericFilterRecoRecoEcalCandidate = cms.EDFilter('HLTEgammaGenericFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltSingleEgammaEtFilter'),
  isoTag = cms.InputTag('hltSingleEgammaHcalIsol'),
  nonIsoTag = cms.InputTag('hltSingleEgammaHcalNonIsol'),
  lessThan = cms.bool(True),
  useEt = cms.bool(False),
  thrRegularEB = cms.double(0),
  thrRegularEE = cms.double(0),
  thrOverEEB = cms.double(-1),
  thrOverEEE = cms.double(-1),
  thrOverE2EB = cms.double(-1),
  thrOverE2EE = cms.double(-1),
  ncandcut = cms.int32(1),
  doIsolated = cms.bool(True),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate')
)
