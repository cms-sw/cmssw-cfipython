import FWCore.ParameterSet.Config as cms

hiFJRhoFlowModulationProducer = cms.EDProducer('HiFJRhoFlowModulationProducer',
  doEvtPlane = cms.bool(False),
  EvtPlane = cms.InputTag('hiEvtPlane'),
  doJettyExclusion = cms.bool(False),
  doFreePlaneFit = cms.bool(False),
  doFlatTest = cms.bool(False),
  jetTag = cms.InputTag('ak4PFJets'),
  pfCandSource = cms.InputTag('particleFlow'),
  evtPlaneLevel = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
