import FWCore.ParameterSet.Config as cms

def ExternalLHEProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
