import FWCore.ParameterSet.Config as cms

hltDQMObjSelector = cms.EDProducer('HLTDQMGsfEleSelector',
  objs = cms.InputTag(''),
  selection = cms.string('et > 5'),
  mightGet = cms.optional.untracked.vstring
)
