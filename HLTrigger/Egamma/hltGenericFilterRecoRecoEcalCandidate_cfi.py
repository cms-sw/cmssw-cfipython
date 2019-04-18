import FWCore.ParameterSet.Config as cms

hltGenericFilterRecoRecoEcalCandidate = cms.EDFilter('HLTEgammaGenericFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltSingleEgammaEtFilter'),
  varTag = cms.InputTag('hltSingleEgammaHcalIsol'),
  lessThan = cms.bool(True),
  useEt = cms.bool(False),
  thrRegularEB = cms.double(0),
  thrRegularEE = cms.double(0),
  thrOverEEB = cms.double(-1),
  thrOverEEE = cms.double(-1),
  thrOverE2EB = cms.double(-1),
  thrOverE2EE = cms.double(-1),
  ncandcut = cms.int32(1),
  l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate')
)
