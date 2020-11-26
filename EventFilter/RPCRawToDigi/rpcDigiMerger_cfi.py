import FWCore.ParameterSet.Config as cms

rpcDigiMerger = cms.EDProducer('RPCDigiMerger',
  inputTagSimRPCDigis = cms.InputTag('simMuonRPCDigis'),
  inputTagTwinMuxDigis = cms.InputTag(''),
  inputTagOMTFDigis = cms.InputTag(''),
  inputTagCPPFDigis = cms.InputTag(''),
  InputLabel = cms.InputTag(' '),
  bxMinTwinMux = cms.int32(-2),
  bxMaxTwinMux = cms.int32(2),
  bxMinOMTF = cms.int32(-3),
  bxMaxOMTF = cms.int32(4),
  bxMinCPPF = cms.int32(-2),
  bxMaxCPPF = cms.int32(2),
  mightGet = cms.optional.untracked.vstring
)
