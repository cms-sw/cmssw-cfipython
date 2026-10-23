import FWCore.ParameterSet.Config as cms

def ExternalLHEProducer(*args, **kwargs):
  mod = cms.EDProducer('ExternalLHEProducer',
    scriptName = cms.FileInPath(''),
    outputFile = cms.string('myoutput'),
    args = cms.required.vstring,
    numberOfParameters = cms.required.uint32,
    nEvents = cms.required.untracked.uint32,
    storeXML = cms.untracked.bool(False),
    generateConcurrently = cms.untracked.bool(False),
    postGenerationCommand = cms.untracked.vstring(),
    nPartonMapping = cms.optional.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
