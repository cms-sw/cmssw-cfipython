import FWCore.ParameterSet.Config as cms

def CITKPFIsolationSumProducerForPUPPI(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
