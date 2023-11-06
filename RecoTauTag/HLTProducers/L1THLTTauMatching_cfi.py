import FWCore.ParameterSet.Config as cms

L1THLTTauMatching = cms.EDProducer('L1THLTTauMatching',
  L1TauTrigger = cms.InputTag('hltL1sDoubleIsoTau40er'),
  JetSrc = cms.InputTag('hltSelectedPFTausTrackPt1MediumIsolationReg'),
  EtMin = cms.double(0),
  ReduceTauContent = cms.bool(True),
  KeepOriginalVertex = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
