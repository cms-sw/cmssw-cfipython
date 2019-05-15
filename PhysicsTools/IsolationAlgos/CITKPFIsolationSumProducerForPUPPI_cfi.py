import FWCore.ParameterSet.Config as cms

CITKPFIsolationSumProducerForPUPPI = cms.EDProducer('CITKPFIsolationSumProducerForPUPPI',
  srcToIsolate = cms.InputTag('no default'),
  srcForIsolationCone = cms.InputTag('no default'),
  puppiValueMap = cms.InputTag('puppi'),
  isolationConeDefinitions = cms.VPSet(
    cms.PSet(),
    cms.PSet(),
    cms.PSet()
  ),
  usePUPPINoLepton = cms.bool(False)
)
