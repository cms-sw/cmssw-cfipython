import FWCore.ParameterSet.Config as cms

hltEgammaDoubleLegCombFilter = cms.EDFilter('HLTEgammaDoubleLegCombFilter',
  saveTags = cms.bool(True),
  firstLegLastFilter = cms.InputTag('firstFilter'),
  secondLegLastFilter = cms.InputTag('secondFilter'),
  nrRequiredFirstLeg = cms.int32(0),
  nrRequiredSecondLeg = cms.int32(0),
  nrRequiredUniqueLeg = cms.int32(0),
  maxMatchDR = cms.double(0.01)
)
