import FWCore.ParameterSet.Config as cms

CITKPFIsolationSumProducer = cms.EDProducer('CITKPFIsolationSumProducer',
  srcToIsolate = cms.InputTag('no default'),
  srcForIsolationCone = cms.InputTag('no default'),
  isolationConeDefinitions = cms.VPSet(
    cms.PSet(),
    cms.PSet(),
    cms.PSet()
  )
)
