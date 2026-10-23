import FWCore.ParameterSet.Config as cms

def CITKPFIsolationSumProducer(*args, **kwargs):
  mod = cms.EDProducer('CITKPFIsolationSumProducer',
    srcToIsolate = cms.InputTag('no default'),
    srcForIsolationCone = cms.InputTag('no default'),
    isolationConeDefinitions = cms.VPSet(
      cms.PSet(),
      cms.PSet(),
      cms.PSet(),
      template = cms.PSetTemplate(
        isolationAlgo = cms.string('no default'),
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('no default'),
        miniAODVertexCodes = cms.vuint32(
          2,
          3
        ),
        VetoConeSizeBarrel = cms.double(0),
        VetoConeSizeEndcaps = cms.double(0),
        vertexIndex = cms.int32(0),
        particleBasedIsolation = cms.InputTag('no default')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
