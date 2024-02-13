import FWCore.ParameterSet.Config as cms

Phase2OTValidateTTStub = cms.EDProducer('Phase2OTValidateTTStub',
  TH2TTStub_RZ = cms.PSet(
    Nbinsx = cms.int32(900),
    xmax = cms.double(300),
    xmin = cms.double(-300),
    Nbinsy = cms.int32(900),
    ymax = cms.double(120),
    ymin = cms.double(0)
  ),
  TopFolderName = cms.string('TrackerPhase2OTStubV'),
  TTStubs = cms.InputTag('TTStubsFromPhase2TrackerDigis', 'StubAccepted'),
  mightGet = cms.optional.untracked.vstring
)
