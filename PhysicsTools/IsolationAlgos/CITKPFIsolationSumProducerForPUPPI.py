import FWCore.ParameterSet.Config as cms

def CITKPFIsolationSumProducerForPUPPI(**kwargs):
  mod = cms.EDProducer('CITKPFIsolationSumProducerForPUPPI',
    srcToIsolate = cms.InputTag('no default'),
    srcForIsolationCone = cms.InputTag('no default'),
    puppiValueMap = cms.InputTag('puppi'),
    isolationConeDefinitions = cms.VPSet(
      cms.PSet(),
      cms.PSet(),
      cms.PSet()
    ),
    usePUPPINoLepton = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
