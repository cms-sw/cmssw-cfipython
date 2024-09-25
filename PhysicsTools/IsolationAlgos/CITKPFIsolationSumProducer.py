import FWCore.ParameterSet.Config as cms

def CITKPFIsolationSumProducer(*args, **kwargs):
  mod = cms.EDProducer('CITKPFIsolationSumProducer',
    srcToIsolate = cms.InputTag('no default'),
    srcForIsolationCone = cms.InputTag('no default'),
    isolationConeDefinitions = cms.VPSet(
      cms.PSet(),
      cms.PSet(),
      cms.PSet()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
